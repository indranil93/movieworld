# -*- coding: utf-8 -*-
# this file is released under public domain and you can use without limitations

#########################################################################
## Customize your APP title, subtitle and menus here
#########################################################################

response.logo = A(B('movieWorld'),XML('&trade;&nbsp;'),
                  _class="navbar-brand",_href=URL('index'),
                  _id="web2py-logo")
response.title = request.application.replace('_',' ').title()
response.subtitle = ''

## read more at http://dev.w3.org/html5/markup/meta.name.html
response.meta.author = 'Your Name <you@example.com>'
response.meta.description = 'a cool new app'
response.meta.keywords = 'web2py, python, framework'
response.meta.generator = 'Web2py Web Framework'

## your http://google.com/analytics id
response.google_analytics_id = None

#########################################################################
## this is the main application menu add/remove items as required
#########################################################################

response.menu = [
    (T('News'), False, URL('default', 'index')),
   # (T('View Reviews'), False, URL('default', 'rlist')),

    ]

if auth.has_membership('Default_User'):
    response.menu.append((T('View Profile'),False,URL('default','viewprofile')))

if auth.has_membership('Default_User'):
    response.menu.append((T('View Messages'),False,URL('default','viewmessages')))

if auth.has_membership('Manager'):
    response.menu.append((T('Manage'),False,URL('default','manage')))

if "auth" in locals(): auth.wikimenu()
