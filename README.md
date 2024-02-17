# Subdomain-Enumeration
utilizing the SecurityTrails API to enumerate all possible subdomains 

## Requirements

- Python 3.x
- `requests` library (`pip install requests`)
- SecurityTrails API key (Sign up at [SecurityTrails](https://securitytrails.com/) to obtain an API key)

## Usage

1. Clone the repository or download the `subdomain_enum.py` file.
2. Install the required dependencies: `pip install requests`
3. Obtain your SecurityTrails API key from [SecurityTrails](https://securitytrails.com/).
4. Run the script using the command `python subdomain_collector.py`.
5. Enter the domain for which you want to enumerate subdomains.
6. Enter your SecurityTrails API key when prompted.
7. Subdomains will be displayed and saved to a file.

## Example

$ python subdomain_enum.py

- Enter the domain: example.com
- Enter your SecurityTrails API key: [Your API Key]
- Enter the filename to save subdomains: example_subdomains.txt
- Subdomains saved to example_subdomains.txt

