
r'''
usage:
    visit http://127.0.0.2:8000/cgi-bin/show_env.py?a=b&k=v

see: http.server.CGIHTTPRequestHandler.run_cgi
    env['XXX'] = ...

env['SERVER_SOFTWARE']
env['SERVER_NAME']
env['GATEWAY_INTERFACE']
env['SERVER_PROTOCOL']
env['SERVER_PORT']
env['REQUEST_METHOD']
env['PATH_INFO']
env['PATH_TRANSLATED']
env['SCRIPT_NAME']
env['QUERY_STRING']
env['REMOTE_ADDR']
env['AUTH_TYPE']
env['REMOTE_USER']
env['CONTENT_TYPE']
env['CONTENT_TYPE']
env['CONTENT_LENGTH']
env['HTTP_REFERER']
env['HTTP_ACCEPT']
env['HTTP_USER_AGENT']
env['HTTP_COOKIE']
env['REMOTE_HOST']


Cookies are a plain text data record of 5 variable-length fields
    Expires − The date the cookie will expire. If this is blank, the cookie will expire when the visitor quits the browser.
    Domain − The domain name of your site.
    Path − The path to the directory or web page that sets the cookie. This may be blank if you want to retrieve the cookie from any directory or page.
    Secure − If this field contains the word "secure", then the cookie may only be retrieved with a secure server. If this field is blank, no such restriction exists.
    Name=Value − Cookies are set and retrieved in the form of key and value pairs.
        # https://stackoverflow.com/questions/1969232/allowed-characters-in-cookies
        1) a sequence of characters excluding semi-colon, comma and white space.
        2) control characters (\x00 to \x1F plus \x7F) aren't allowed
        3) browsers are totally inconsistent about, is non-ASCII (Unicode) characters
        4) avoid 'Name=Value'.count('=') != 1
            although ==0 and >=2 are allowed.
            'Value' <==> '=Value' <==> {'name':'', 'value':'Value'}
            'Name=Value=Value' <==> {'name':'Name', 'value':'Value=Value'}



below code see:
    http://www.tutorialspoint.com/python/python_cgi_programming.htm
'''


keys = frozenset('''
    SERVER_SOFTWARE
    SERVER_NAME
    GATEWAY_INTERFACE
    SERVER_PROTOCOL
    SERVER_PORT
    REQUEST_METHOD
    PATH_INFO
    PATH_TRANSLATED
    SCRIPT_NAME
    QUERY_STRING
    REMOTE_ADDR
    AUTH_TYPE
    REMOTE_USER
    CONTENT_TYPE
    CONTENT_TYPE
    CONTENT_LENGTH
    HTTP_REFERER
    HTTP_ACCEPT
    HTTP_USER_AGENT
    HTTP_COOKIE
    REMOTE_HOST
    '''.split())




if True:
    #[optional] Setting up Cookies
    #print "Set-Cookie:UserID = XYZ;\r\n"
    #print "Set-Cookie:Password = XYZ123;\r\n"
    #print "Set-Cookie:Expires = Tuesday, 31-Dec-2007 23:12:40 GMT";\r\n"
    #print "Set-Cookie:Domain = www.tutorialspoint.com;\r\n"
    #print "Set-Cookie:Path = /perl;\n"
    print('Set-Cookie:abc = 123;')
    print('Set-Cookie:uuu = kkk;')
print("Content-type: text/html")
print()

import os
print("<h1>Environment</h1><br/>")
for key, value in os.environ.items():
    if key in keys:
        print(f"<b>{key: <20}</b>: {value}<br/>")


print('<br/>')
print("<h1>Cookies</h1><br/>")
str_cookies = os.environ.get('HTTP_COOKIE', '')
for str_pair in str_cookies.split(';'):
    key, value = str_pair.split('=')
    print(f"<b>Cookies['{key: <20}']</b> = {value}<br/>")



import cgi
form = cgi.FieldStorage(keep_blank_values=True)
print('<br/>')
print("<h1>FieldStorage</h1><br/>")
print(f"<b>QUERY_STRING</b>: {os.environ['QUERY_STRING']}<br/>")
for key in form.keys():
    # QUERY_STRING if GET
    value = form.getvalue(key)
    if os.environ['REQUEST_METHOD'].upper() == 'GET':
        print(f"<b>QUERY_STRING['{key: <20}']</b> = {value}<br/>")
    else:
        print(f"<b>post_form['{key: <20}']</b> = {value}<br/>")

print('<br/>')
print("<h1>File Received</h1><br/>")

#NOTE:
#   form[key] is not form.getvalue(key)!!
#   form[key] -> FieldStorage|[FieldStorage]
#   form.getvalue(key, default) -> default|FieldStorage.value|[FieldStorage.value]
#   form.getfirst(key, default) -> default|FieldStorage.value
#   form.getlist(key) -> [FieldStorage.value]
#
if 'XXX_filename' in form:
    XXX_filename_item_or_ls = form['XXX_filename']
    if isinstance(XXX_filename_item_or_ls, list):
        XXX_filename_items = XXX_filename_item_or_ls
    else:
        XXX_filename_item = XXX_filename_item_or_ls
        XXX_filename_items = [XXX_filename_item]
else:
    XXX_filename_items = []
for XXX_filename_item in XXX_filename_items:
    print(f"<b>XXX_filename_item.filename</b>: {XXX_filename_item.filename}<br/>")
    print(f"<b>XXX_filename_item.file.read()</b>: {XXX_filename_item.file.read()}<br/>")



print('''
<h1>GET</h1>
<form action = "/cgi-bin/show_env.py" method = "get">
    # will GET http://...?first_name=xxxx&last_name=yyyy
    #vs below method = "post"
    # will POST http://...
    First Name:
        <input type = "text" name = "first_name" />
        <br />
    Last Name:
        <input type = "text" name = "last_name" />
        <br />
    <input type = "submit" value = "Submit" />
</form>
''')


print('''
<h1>POST</h1>
<form action = "/cgi-bin/show_env.py" method = "post">
    # will POST http://...
    First Name:
        <input type = "text" name = "first_name" />
        <br />
    Last Name:
        <input type = "text" name = "last_name" />
        <br />
    <input type = "submit" value = "Submit" />
</form>
''')

print('''
<h1>POST</h1>
<form action = "/cgi-bin/show_env.py" method = "post" target = "_blank">
    # will POST http://...
    <h3>subject</h3>
    <input type = "radio" name = "subject" value = "maths" /> Maths
    <input type = "radio" name = "subject" value = "physics" /> Physics

    <h3>select subject</h3>
    <input type = "checkbox" name = "maths" value = "the_selected_value for Maths" /> Maths
    <input type = "checkbox" name = "physics" value = "the_selected_value for Physics" /> Physics

    <h3>textcontent</h3>
    <textarea name = "textcontent" cols = "40" rows = "4">
    Type your text here...
    </textarea>

    <h3>dropdown_select</h3>
    <select name = "dropdown">
        <option value = "Maths" selected>Maths</option>
        <option value = "Physics">Physics</option>
    </select>

    <br/>
    <input type = "submit" value = "Submit" />
</form>
''')

print('''
<h1>POST: file-upload # enctype=multipart/form-data"</h1>
<form action = "/cgi-bin/show_env.py" method = "post" target = "_blank"
    enctype = "multipart/form-data"
    >

   <p>select file: <input type = "file" name = "XXX_filename" /></p>

   <p><input type = "submit" value = "Upload" /></p>
</form>
''')


