# -*- coding:utf-8 -*-

def get_another_size_profile_image_url(url, variant):
    """
    Variant  Dimentions
    ---------------------
    normal   48px by 48px
    bigger   73px by 73px
    mini     24px by 24px
    original original
    """
    normal = 'normal'
    bigger = 'bigger'
    mini = 'mini'
    original = 'original'
    if variant not in (normal, bigger, mini, original):
        raise ValueError('Variant is invalid.')

    idx = url.rfind('.')
    if idx == -1:
        # no extension (.jpg, .png)
        return url

    for suffix in ('_{0}'.format(x) for x in (normal, bigger, mini)):
        if url[:idx].endswith(suffix):
            prefix = url[:idx][:-1 * len(suffix)]
            if variant == original:
                return prefix + url[idx:]
            else:
                return '{0}_{1}{2}'.format(prefix, variant, url[idx:])
    # url is original-format
    prefix = url[:idx]
    if variant == original:
        return prefix + url[idx:]
    else:
        return '{0}_{1}{2}'.format(prefix, variant, url[idx:])
