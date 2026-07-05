$readme = "C:\Users\ishan\Documents\Projects\Awesome-Depth-Estimation\README.md"
$folder = "Awesome-Depth-Estimation"
$starHistory = @"

##  Star History
<div align="center">
<a href="https://www.star-history.com/?repos=ishandutta2007%2F$folder&type=date&legend=bottom-right">
<picture>
<source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/$folder&type=date&theme=dark&legend=bottom-right" />
<source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=ishandutta2007/$folder&type=date&legend=bottom-right" />
<img alt="Star History Chart" src="https://api.star-history.com/chart?repos=ishandutta2007/$folder&type=date&legend=bottom-right" />
</picture>
</a>
</div>
"@

Add-Content -Path $readme -Value $starHistory
git add .
git commit -m "star history added"
git push

(Get-Content $readme) -replace 'chartrepos', 'chart?repos' | Set-Content $readme
git add .
git commit -m "fixed star plot"
git push

(Get-Content $readme) -replace 'https://github.com/sindresorhus/awesome', 'https://github.com/ishandutta2007/Awesome-Awesome-Awesome' | Set-Content $readme
git add .
git commit -m "invalid awesome link fixed"
git push
