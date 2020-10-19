echo 'host    all             postgres        172.17.0.0/16           password' >> /var/lib/postgresql/data/pg_hba.conf
echo "host all  all    0.0.0.0/0  md5" >> /var/lib/postgresql/data/pg_hba.conf
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" <<EOF
CREATE EXTENSION IF NOT EXISTS pgagent;
EOF
