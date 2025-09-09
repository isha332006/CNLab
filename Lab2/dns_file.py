import dns.resolver

def dns_lookup(domain):
    with open("dns_log.txt", "w") as log:
        for rtype in ['A','MX','CNAME']:
            try:
                answers=dns.resolver.resolve(domain, rtype)
                print(f"{rtype} record(s) for {domain}:")
                for rdata in answers:
                    print(f"{rdata}") # Write to console
                    log.write(f"{rtype} Record: {rdata}\n") # Write to log file
            except Exception as e:
                error_msg=f"{rtype} Record query failed: {e}"
                print(error_msg)
                log.write(error_msg +"\n")

dns_lookup("google.com")
