FROM 172.16.210.227:11443/library/ubuntu-22.04:v1.0-python310

ARG WORKSPACE="/llm-sd-api"

WORKDIR $WORKSPACE

COPY requirements.txt $WORKSPACE/requirements.txt
COPY start.sh $WORKSPACE/start.sh
ARG PIP_INSTALL="pip install --no-cache-dir -i http://172.16.210.191:39961/simple/ --trusted-host 172.16.210.191 "
RUN pip install -r requirements.txt \
    && rm -rf $WORKSPACE/requirements.txt \
    && chmod +x $WORKSPACE/start.sh \
    && pip install sqlalchemy==2.0.31.dev0 -i

COPY app $WORKSPACE/app
COPY static $WORKSPACE/static

CMD bash /llm-sd-api/start.sh


