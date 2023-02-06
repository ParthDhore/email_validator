from flask_restful import Resource
import re
import smtplib
import dns.resolver

class email_val(Resource):
    def get(self,email):
        from_address='test@example.com'

        # Simple Regex for syntax checking
        regex = '^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,})$'
        to_address=email
        match = re.match(regex, to_address)
        if match == None:
            return False
        
        # Get domain for DNS lookup
        splitAddress = to_address.split('@')
        domain = str(splitAddress[1])

        if domain=='yahoo.com':
            return "functionality removed"

        else:
            # MX record lookup
            records = dns.resolver.resolve(domain, 'MX')
            mxRecord = records[0].exchange
            mxRecord = str(mxRecord)


            # SMTP lib setup (use debug level for full output)
            server = smtplib.SMTP()
            server.set_debuglevel(0)

            # SMTP Conversation
            server.connect(mxRecord)
            server.helo(server.local_hostname) ### server.local_hostname(Get local server hostname)
            server.mail(from_address)
            code, message = server.rcpt(str(to_address))
            server.quit()
            if code==250:
                return True
            else:
                return False
