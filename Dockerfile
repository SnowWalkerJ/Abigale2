FROM node:8 as AbiWeb
RUN mkdir /data
ADD AbiWeb /data
WORKDIR /data
RUN npm install
RUN npm run build


FROM python:3.6-alpine
EXPOSE 8080

RUN mkdir -p /data/web
ADD AbiAPI /data
WORKDIR /data
COPY --from=AbiWeb /data/index_prod.html ./web
COPY --from=AbiWeb /data/dist ./web/dist
RUN pip install -r requirements.txt --index-url https://pypi.douban.com/simple --trusted-host pypi.douban.com

CMD ["python", "app.py", "run", "--port", "8080", "--host", "0.0.0.0"]
