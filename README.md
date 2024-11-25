# EX01 Developing a Simple Webserver

# Date: 25 - 11 - 2024
# AIM:
To develop a simple webserver to serve html pages and display the configuration details of laptop.

# DESIGN STEPS:
## Step 1:
HTML content creation.

## Step 2:
Design of webserver workflow.

## Step 3:
Implementation using Python code.

## Step 4:
Serving the HTML pages.

## Step 5:
Testing the webserver.

# PROGRAM:
settings.py 
```
import os
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'simpleserver'
]
```
views.py
```
from django.http import HttpResponse

def systemInfo (request):
    host = request.get_host()
    port = host.split(':')[1]
    print(f'The server is running on the port {port}')
    print('GET request received...')
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
    response = HttpResponse(html_content, status=200) 
    print(f'Status code {response.status_code}')
    print('HTML response sent successfully.')
    
    return response 
 
```
Django app's urls.py 
```
from django.urls import path
from .views import systemInfo

urlpatterns = [
    path('', systemInfo, name='system_info'),
]
```
Django project's urls.py 
```
from django.contrib import admin
from django.urls import path,include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('simpleserver.urls'))
]

```


# OUTPUT:
### Browser 
![image](https://github.com/user-attachments/assets/b8ca58db-349e-4386-9b19-f0af70b49720)

### Terminal 
![image](https://github.com/user-attachments/assets/217b6978-527f-4ed5-8eee-90c84679de1b)


# RESULT:
The program for implementing simple webserver is executed successfully.
