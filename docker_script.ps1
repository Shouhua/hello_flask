$Timestamp = Get-Date -Format "yyyyMMddHHmmss"

$HelloApp = "ampregistry:5000/hello_app:$Timestamp"

Write-Host $HelloApp

docker build -f .\Dockerfile -t $HelloApp .
docker push $HelloApp