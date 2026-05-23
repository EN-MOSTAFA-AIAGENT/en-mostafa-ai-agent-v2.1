import requests

class WPManager:
    def __init__(self):
        self.sites = []

    def list_sites(self):
        return self.sites

    def get_site_status(self, site_name):
        for site in self.sites:
            if site['name'] == site_name:
                return {'name': site_name, 'status': 'connected', 'url': site['url']}
        return {'error': 'site not found'}

    def add_site(self, name, url, api_key=None):
        self.sites.append({'name': name, 'url': url, 'api_key': api_key})
        return {'success': True, 'site': name}
