FROM hayd/alpine-deno:1.8.3
WORKDIR /app
USER deno
COPY . .
RUN deno cache ./src/app.ts
EXPOSE 3001
CMD ["run", "--allow-net", "--allow-env", "./src/app.ts"]
