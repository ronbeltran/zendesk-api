Zendesk API Python Wrapper
--------------------------

Supports client credentials grant type for now

Usage:

    $ python
    Python 2.7.6 (default, Mar 22 2014, 22:59:56) 
    [GCC 4.8.2] on linux2
    Type "help", "copyright", "credits" or "license" for more information.
    >>> import zendeskapi
    >>> zd=zendeskapi.Zendesk('replace_with_client_id', 'replace_with_client_secret', 'replace_with_company_name')
    >>> print zd.oauth_login()
    (200, {u'access_token': u'access-token-here', u'token_type': u'bearer', u'scope': u'read'})
    >>> 
