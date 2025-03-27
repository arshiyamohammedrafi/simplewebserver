from http.server import HTTPServer,BaseHTTPRequestHandler

content='''

<!DOCTYPE html>
<html>
<head>
    <title>TCP/IP Layers and Protocols</title>
    
        
</head>
<body>
    <h2>TCP/IP Layers and Protocols</h2>
    <table border="1">
        <tr>
            <th>TCP/IP Layers</th>
            <th>Protocols (Examples)</th>
        </tr>
        <tr>
            <td>Application Layer</td>
            <td>HTTP, RDP, DNS, SMTP, Telnet, SNMP</td>
        </tr>
        <tr>
            <td>Transport Layer</td>
            <td>TCP, UDP</td>
        </tr>
        <tr>
            <td>Internet Layer</td>
            <td>ICMP, IGMP, ARP, IP, IPSec</td>
        </tr>
        <tr>
            <td>Network Access Layer</td>
            <td>Ethernet (IEEE 802.3), Token Ring, PPP, Frame Relay</td>
        </tr>
    </table>
</body>
</html>
'''

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        print("Get request received...")
        self.send_response(200) 
        self.send_header("content-type", "text/html")       
        self.end_headers()
        self.wfile.write(content.encode())

print("This is my webserver") 
server_address =('',8000)
httpd = HTTPServer(server_address,MyServer)
httpd.serve_forever()