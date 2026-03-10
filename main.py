import argparse
import sys
from utils.printer import Printer
from core.engine import SQLiEngine

def main():
    Printer.show_banner()
    
    parser = argparse.ArgumentParser(
        description='SQLPwn - Advanced SQL Injection Framework',
        epilog='Author: Bahrul Rozak | GitHub: @bahrul-rozak',
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('-u', '--url', required=True, help='Target URL (e.g., http://example.com/page.php?id=1)')
    parser.add_argument('-m', '--method', choices=['GET', 'POST'], default='GET', help='HTTP method (default: GET)')
    parser.add_argument('-p', '--param', help='Specific parameter to test')
    parser.add_argument('--delay', type=float, default=0, help='Delay between requests in seconds')
    parser.add_argument('--timeout', type=int, default=10, help='Request timeout in seconds')
    
    parser.add_argument('--error-based', action='store_true', help='Test error-based injection')
    parser.add_argument('--union-based', action='store_true', help='Test union-based injection')
    parser.add_argument('--blind-based', action='store_true', help='Test blind injection')
    parser.add_argument('--all', action='store_true', help='Run all tests')
    
    parser.add_argument('--dump', action='store_true', help='Attempt to dump database (requires vulnerability)')
    parser.add_argument('--tables', help='Specify tables to dump (comma-separated)')
    
    parser.add_argument('-v', '--verbose', action='store_true', help='Verbose output')
    parser.add_argument('--version', action='version', version='SQLPwn 1.0.0')
    
    if len(sys.argv) == 1:
        parser.print_help()
        sys.exit(1)
    
    args = parser.parse_args()
    
    Printer.print_info(f"Target: {args.url}")
    Printer.print_info(f"Method: {args.method}")
    
    engine = SQLiEngine(
        url=args.url,
        method=args.method,
        param=args.param,
        delay=args.delay
    )
    
    if args.error_based or args.all:
        engine.test_error_based()
    
    if args.union_based or args.all:
        Printer.print_warning("Union-based testing not yet implemented")
    
    if args.blind_based or args.all:
        Printer.print_warning("Blind-based testing not yet implemented")
    
    if args.dump and engine.vulnerable_params:
        Printer.print_info("Dump feature coming soon...")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        Printer.print_warning("\nScan interrupted by user")
        sys.exit(0)
    except Exception as e:
        Printer.print_error(f"Error: {str(e)}")
        sys.exit(1)