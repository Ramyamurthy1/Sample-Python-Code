#####
# SCRIPT TO UPDATE URLS

##########################

EKS_NAMESPACE="cyswy001n-ns-ib-orch-001"

aws eks --region us-east-2 update-kubeconfig --name $EKS_CLUSTER
kubectl get $EKS_NAMESPACE

echo "Inside update script"

kubectl get secret ib-orc-230-strimzi-001-cluster-ca-cert -o "jsonpath={.data['ca\.crt']}" -n $EKS_NAMESPACE | base64 -d > ca.crt
cat ca.crt

cicd_Dashboard=$(kubectl -n $EKS_NAMESPACE get ingress | grep -E 'cicd' | awk '{ print $4 }')
KAMI_END_POINT=$(kubectl -n $EKS_NAMESPACE get ingress | grep -E 'tmf-core' | awk '{ print $4 }')

KAMIURL=https://$KAMI_END_POINT/KamiCore/api/serviceOrder"'"
KAMI_URL=$KAMIURL
auth_url=https://$KAMI_END_POINT/KamiCore/oauth/token?grant_type=client_credentials"'"
event_logger_url=https://$(kubectl -n $EKS_NAMESPACE get ingress | grep -E 'event-logger' | awk '{ print $4 }')/evntLogger/get/events?external_order_id="'"
kafka_svc=$(kubectl -n $EKS_NAMESPACE get svc| grep -E 'kafka-bootstrap'|awk '{ print $1 }'):9092"'"
cat token_urls.py

sed -i -r "s#^(AUTH_TOKEN_URL=').*#\1${auth_url//#/\\#}#" token_urls.py

sed -i -r "s#^(KAMI_ENDPOINT=').*#\1${KAMIURL//#/\\#}#" token_urls.py

sed -i -r "s#^(KAFKA_URL=').*#\1${kafka_svc//#/\\#}#" token_urls.py

sed -i -r "s#^(EVENT_LOGGER_URL=').*#\1${event_logger_url//#/\\#}#" token_urls.py
~
