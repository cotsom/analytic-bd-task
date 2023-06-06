FROM postgres:13.3

WORKDIR /app

COPY datasets datasets
COPY initdb.sh initdb.sh
# CMD [ "/app/initdb.sh" ]
# RUN psql -U root -d technique -c "select * from products;"
# RUN psql -U root -d technique -c "\dt"