import requests

def get_subdomains(domain, api_key):
    url = f"https://api.securitytrails.com/v1/domain/{domain}/subdomains"
    headers = {"APIKEY": api_key}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        subdomains = data.get('subdomains', [])
        return subdomains
    else:
        print(f"Error: {response.status_code}")
        return []

def save_subdomains_to_file(subdomains, filename):
    with open(filename, 'w') as file:
        for subdomain in subdomains:
            file.write(subdomain + '\n')

def main():
    domain = input("Enter the domain: ")
    api_key = input("Enter your SecurityTrails API key: ")

    subdomains = get_subdomains(domain, api_key)
    if subdomains:
        print(f"Subdomains of {domain}:")
        for subdomain in subdomains:
            print(subdomain)
        
        filename = input("Enter the filename to save subdomains: ")
        save_subdomains_to_file(subdomains, filename)
        print(f"Subdomains saved to {filename}")
    else:
        print("No subdomains found.")

if __name__ == "__main__":
    main()
