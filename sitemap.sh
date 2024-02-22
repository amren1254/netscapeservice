#!/bin/bash

# Set the website URL
website_url="https://netscapeservice.com"

# Set the output file for the sitemap
sitemap_file="sitemap.xml"

# Fetch the HTML content using curl and parse with pup
html_content=$(curl -s "$website_url" | pup 'a attr{href}')

# Create the sitemap.xml file using xmlstarlet
echo '<?xml version="1.0" encoding="UTF-8"?>' > "$sitemap_file"
echo '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' >> "$sitemap_file"

for url in $html_content; do
  echo "  <url><loc>$url</loc></url>" >> "$sitemap_file"
done

echo '</urlset>' >> "$sitemap_file"

echo "Sitemap generated successfully at $sitemap_file"
