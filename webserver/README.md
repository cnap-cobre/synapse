This is a container that reverse proxies a TLS localhost to non-tls localhost.

This is necessary for testing OAuth2/OpenID Connect endpoints because the specification requires
all redirect urls to be secure.  And http://localhost/accounts/cilogon/login/callback/ is not secure.
