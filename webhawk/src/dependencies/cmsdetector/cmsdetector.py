# cms-detector
import requests


# Mask the user agent so it doesn't show as python and get blocked, set global for request that need to allow for redirects
# Get function to swap the user agent

user_agent = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.116 Safari/537.36',
}


def get(domain):
    return requests.get(domain, allow_redirects=False, headers=user_agent)


def wordpress(domain):
    ####################################################
    # WordPress Scans
    ####################################################

    # Use requests.get allowing redirects otherwise will always fail
    detected = 0
    wpLoginCheck = requests.get(
        domain + '/wp-login.php', headers=user_agent)
    if (wpLoginCheck.status_code == 200 and "user_login" in wpLoginCheck.text and "404" not in wpLoginCheck.text):
        detected += 1

    # Use requests.get allowing redirects otherwise will always fail
    wpAdminCheck = requests.get(
        domain + '/wp-admin', headers=user_agent)
    if (wpAdminCheck.status_code == 200 and "user_login" in wpAdminCheck.text and "404" not in wpLoginCheck.text):
        detected += 1

    wpAdminUpgradeCheck = get(domain + '/wp-admin/upgrade.php')
    if (wpAdminUpgradeCheck.status_code == 200 and "404" not in wpAdminUpgradeCheck.text):
        detected += 1

    wpAdminReadMeCheck = get(domain + '/readme.html')
    if (wpAdminReadMeCheck.status_code == 200 and "404" not in wpAdminReadMeCheck.text):
        detected += 1

    wpLinksCheck = get(domain)
    if ('wp-' in wpLinksCheck.text):
        detected += 1

    if (detected != 0):
        return 1


def joomla(domain):
    ####################################################
    # Joomla Scans
    ####################################################

    detected = 0
    joomlaAdminCheck = get(domain + '/administrator/')
    if (joomlaAdminCheck.status_code == 200 and "mod-login-username" in joomlaAdminCheck.text and "404" not in joomlaAdminCheck.text):
        detected += 1

    joomlaReadMeCheck = get(domain + '/readme.txt')
    if (joomlaReadMeCheck.status_code == 200 and "joomla" in joomlaReadMeCheck.text and "404" not in joomlaReadMeCheck.text):
        detected += 1

    joomlaTagCheck = get(domain)
    if (joomlaTagCheck.status_code == 200 and 'name="generator" content="Joomla' in joomlaTagCheck.text and "404" not in joomlaTagCheck.text):
        detected += 1

    joomlaStringCheck = get(domain)
    if (joomlaStringCheck.status_code == 200 and "joomla" in joomlaStringCheck.text and "404" not in joomlaStringCheck.text):
        detected += 1

    joomlaDirCheck = get(domain + '/media/com_joomlaupdate/')
    if (joomlaDirCheck.status_code == 403 and "404" not in joomlaDirCheck.text):
        detected += 1

    if (detected != 0):
        return 1


def magento(domain):
    ####################################################
    # Magento Scans
    ####################################################

    detected = 0
    magentoAdminCheck = get(domain + '/index.php/admin/')
    if (magentoAdminCheck.status_code == 200 and 'login' in magentoAdminCheck.text and "404" not in magentoAdminCheck.text):
        detected += 1

    magentoRelNotesCheck = get(domain + '/RELEASE_NOTES.txt')
    if (magentoRelNotesCheck.status_code == 200 and 'magento' in magentoRelNotesCheck.text):
        detected += 1

    magentoCookieCheck = get(domain + '/js/mage/cookies.js')
    if (magentoCookieCheck.status_code == 200 and "404" not in magentoCookieCheck.text):
        detected += 1

    magStringCheck = get(domain + '/index.php')
    if (magStringCheck.status_code == 200 and '/mage/' in magStringCheck.text or 'magento' in magStringCheck.text):
        detected += 1

    magentoStylesCSSCheck = get(
        domain + '/skin/frontend/default/default/css/styles.css')
    if (magentoStylesCSSCheck.status_code == 200 and "404" not in magentoStylesCSSCheck.text):
        detected += 1

    mag404Check = get(domain + '/errors/design.xml')
    if (mag404Check.status_code == 200 and "magento" in mag404Check.text):
        detected += 1

    if (detected != 0):
        return 1


def drupal(domain):
    ####################################################
    # Drupal Scans
    ####################################################

    detected = 0
    drupalReadMeCheck = get(domain + '/readme.txt')
    if drupalReadMeCheck.status_code == 200 and 'drupal' in drupalReadMeCheck.text and '404' not in drupalReadMeCheck.text:
        detected += 1

    drupalTagCheck = get(domain)
    if drupalTagCheck.status_code == 200 and 'name="Generator" content="Drupal' in drupalTagCheck.text:
        detected += 1

    drupalCopyrightCheck = get(domain + '/core/COPYRIGHT.txt')
    if drupalCopyrightCheck.status_code == 200 and 'Drupal' in drupalCopyrightCheck.text and '404' not in drupalCopyrightCheck.text:
        detected += 1

    drupalReadme2Check = get(domain + '/modules/README.txt')
    if drupalReadme2Check.status_code == 200 and 'drupal' in drupalReadme2Check.text and '404' not in drupalReadme2Check.text:
        detected += 1

    drupalStringCheck = get(domain)
    if drupalStringCheck.status_code == 200 and 'drupal' in drupalStringCheck.text:
        detected += 1

    if (detected != 0):
        return 1


def phpmyadmin(domain):
    ####################################################
    # phpMyAdmin Scans
    ####################################################

    detected = 0
    phpMyAdminCheck = get(domain)
    if phpMyAdminCheck.status_code == 200 and 'phpmyadmin' in phpMyAdminCheck.text:
        detected += 1

    pmaCheck = get(domain)
    if pmaCheck.status_code == 200 and 'pmahomme' in pmaCheck.text or 'pma_' in pmaCheck.text:
        detected += 1

    phpMyAdminConfigCheck = get(domain + '/config.inc.php')
    if phpMyAdminConfigCheck.status_code == 200 and '404' not in phpMyAdminConfigCheck.text:
        detected += 1

    if (detected != 0):
        return 1


def scan(domain):
    if (wordpress(domain) == 1):
        return "Wordpress"
    elif (joomla(domain) == 1):
        return "Joomla"
    elif (magento(domain) == 1):
        return "Magento"
    elif (drupal(domain) == 1):
        return "Drupal"
    elif (phpmyadmin(domain) == 1):
        return "PHPMyAdmin"
    else:
        return None
