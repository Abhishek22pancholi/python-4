
msg_template="""<h1>Hello {name},<h1>
<hr> 
<p>Thx you for joining {website}. We are very happy to have <strong>You</strong> with us!</p>
"""

def format_msg(my_name="Noname", my_website="csh.pl" ):
    my_msg=msg_template.format(name=my_name, website=my_website)
    return my_msg
    
