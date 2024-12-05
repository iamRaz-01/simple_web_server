from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    html_content = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>System Information</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    margin: 0;
                    padding: 0;
                    background: linear-gradient(to right, #4facfe, #00f2fe);
                    color: #333;
                }
                .container {
                    width: 90%;
                    max-width: 800px;
                    margin: 50px auto;
                    background: #fff;
                    border-radius: 10px;
                    box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                    overflow: hidden;
                }
                .header {
                    background: #0078d7;
                    color: #fff;
                    padding: 15px;
                    text-align: center;
                    font-size: 24px;
                    font-weight: bold;
                }
                .content {
                    padding: 20px;
                }
                .details {
                    margin-bottom: 20px;
                }
                .details h3 {
                    margin: 10px 0;
                    color: #0078d7;
                    font-size: 20px;
                }
                .details p {
                    margin: 5px 0;
                    font-size: 16px;
                }
                .footer {
                    background: #f1f1f1;
                    text-align: center;
                    padding: 10px;
                    font-size: 14px;
                }
            </style>
        </head>
        <body>
            <div class="container">
                <div class="header">System Information</div>
                <div class="content">
                    <div class="details">
                        <h3>OS Details</h3>
                        <p><strong>OS Name:</strong> Microsoft Windows 11 Home Single Language</p>
                        <p><strong>Version:</strong> 10.0.26100 Build 26100</p>
                        <p><strong>Other OS Description:</strong> Not Available</p>
                        <p><strong>OS Manufacturer:</strong> Microsoft Corporation</p>
                    </div>
                    <div class="details">
                        <h3>System Details</h3>
                        <p><strong>System Name:</strong> ABDULRAZAK</p>
                        <p><strong>System Manufacturer:</strong> TIMI</p>
                        <p><strong>System Model:</strong> Mi NoteBook Ultra</p>
                        <p><strong>System Type:</strong> x64-based PC</p>
                        <p><strong>Processor:</strong> 11th Gen Intel(R) Core(TM) i5-11320H @ 3.20GHz</p>
                    </div>
                    <div class="details">
                        <h3>Memory</h3>
                        <p><strong>Installed Physical Memory (RAM):</strong> 16.0 GB</p>
                        <p><strong>Total Physical Memory:</strong> 15.8 GB</p>
                        <p><strong>Available Physical Memory:</strong> 5.65 GB</p>
                        <p><strong>Total Virtual Memory:</strong> 16.8 GB</p>
                        <p><strong>Available Virtual Memory:</strong> 4.10 GB</p>
                        <p><strong>Page File:</strong> C:\pagefile.sys</p>
                    </div>
                    <div class="details">
                        <h3>Security</h3>
                        <p><strong>Kernel DMA Protection:</strong> On</p>
                        <p><strong>Virtualization-Based Security:</strong> Not enabled</p>
                        <p><strong>App Control for Business:</strong> Enforced</p>
                    </div>
                </div>
                <div class="footer">© 2024 Abdul Razak's System Info Viewer</div>
            </div>
        </body>
        </html>
    """
        
    def do_GET(self):
        content = self.html_content
        print("Request received")
        self.send_response(200)
        self.send_header('Content-Type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())

# Define server address and port
server_address = ('', 8000)  # Host on all available IPs, port 8000
httpd = HTTPServer(server_address, MyHandler)

print("My webserver is running...")
httpd.serve_forever()
