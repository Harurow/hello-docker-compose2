FROM hayd/alpine-deno:latest
WORKDIR /app
USER deno
COPY . .
RUN deno cache app.ts
EXPOSE 3001
CMD ["run", "--allow-net", "--allow-env", "app.ts"]
