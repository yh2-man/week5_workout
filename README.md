# Simple API + Nginx

- `/` → Nginx 정적 페이지
- `/api/*` → FastAPI (uvicorn)

## 실행
```bash
docker compose up -d --build


브라우저: http://localhost:8080/

API: http://localhost:8080/api/health

API: http://localhost:8080/api/hello?name=Student



위 구조대로 파일 생성  
2. PowerShell에서 폴더로 이동:
   ```powershell
   cd .\simple-api-nginx
   docker compose up -d --build