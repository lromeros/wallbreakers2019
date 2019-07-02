class Solution:
    def get_subdomains(self, d):
        domains = d.split('.')
        subdomains = []
        last_elem = []
        
        for i in range(len(domains)):
            last_elem.insert(0, domains[len(domains) - 1 - i])
            sd = '.'.join(last_elem) if len(last_elem) > 1 else ''.join(last_elem)
            subdomains.append(sd)
            
        return subdomains
        
        
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        sd_counts = {}
        
        for entry in cpdomains:
            count, domain = entry.split(' ')
            count = int(count)
            subdomains = self.get_subdomains(domain)
            
            for sd in subdomains:
                sd_counts[sd] = sd_counts.get(sd, 0) + count
                
        return ["{} {}".format(count, domain) for domain, count in sd_counts.items()]
