# Auto-inventory update script for Aerospace Engineering sources
Write-Host "Updating sources inventory and subject README trackers..." -ForegroundColor Cyan
python "$PSScriptRoot\update_inventory.py"
Write-Host "Inventories updated successfully!" -ForegroundColor Green
