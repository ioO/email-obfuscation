Email obfuscation
=================

Simple python cli to generate html entities to obfuscate email address.

##Usage
    ```bash
    [user@host]$ python email-obfuscation.py -h

    usage: email-obfuscation.py [-h] [-m] email

    Generate a string to obfuscate your email address

    positional arguments:
    email              email address to obfuscate

    optional arguments:
    -h, --help         show this help message and exit
    -m, --with-mailto  Return a string link with mailto obfuscated
    ```

Return a simple string of mixed html entities with ascii decimal and with ascii hexadecimal
    ```bash
    [user@host]$ python email-obfuscation.py user@example.com
    Email address obfuscated:
    &#117;&#115;&#101;&#x72;&#64;&#x65;&#x78;&#97;&#x6d;&#x70;&#108;&#101;&#x2e;&#x63;&#111;&#109;
    ```

Do it twice to have a different address obfuscation for *href* and link text.
    ```html
    <a href="mailto:&#117;&#115;&#101;&#x72;&#64;&#x65;&#x78;&#97;&#x6d;&#x70;&#108;&#101;&#x2e;&#x63;&#111;&#109;">
    &#117;&#x73;&#x65;&#x72;&#x40;&#x65;&#120;&#x61;&#109;&#112;&#108;&#x65;&#x2e;&#x63;&#111;&#109;</a>
    ```

With *-m* or *--with-mailto* it returns first the email address obfuscated and second the link you put in href
    ```bash
    [user@host]$ python email-obfuscation.py --with-mailto user@example.com
    Email address obfuscated:
    &#117;&#x73;&#101;&#114;&#x40;&#101;&#120;&#x61;&#x6d;&#112;&#108;&#x65;&#46;&#99;&#111;&#x6d;
    mailto link obfuscated :
    &#x6d;&#x61;&#x69;&#x6c;&#116;&#111;&#58;&#x75;&#x73;&#101;&#x72;&#x40;&#101;&#120;&#97;&#109;&#112;&#x6c;&#101;&#x2e;&#x63;&#111;&#109;
    ```
Use email address obfuscated for link text and mailto link obfuscated for *href*
    ```html
    <a 
    href="&#x6d;&#x61;&#x69;&#x6c;&#116;&#111;&#58;&#x75;&#x73;&#101;&#x72;&#x40;&#101;&#120;&#97;&#109;&#112;&#x6c;&#101;&#x2e;&#x63;&#111;&#109;">
    &#117;&#x73;&#101;&#114;&#x40;&#101;&#120;&#x61;&#x6d;&#112;&#108;&#x65;&#46;&#99;&#111;&#x6d;</a>
    ```
