# $${\color{orange}Basic discord webhook with discord.py}$$ 


• Put the webhook and website url.
```py
webhook_url = "webhook_url"
website_url = 'website_url'
```

• Select the html elements with using css properties.

```py
article_text = soup.select('div > ol > li > a')
```

• Adjust your message

```py
data = {
    "content": f"# [New notification]({website_url})"
}
```
