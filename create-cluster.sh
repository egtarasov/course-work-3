service_account=?
subnets=?
admin_password=?

yc managed-airflow cluster create \
   --name course-work \
   --admin-password $admin_password \
   --service-account-id $service_account \
   --subnet-ids $subnets \
   --webserver count=1,resource-preset-id=c1-m2 \
   --scheduler count=1,resource-preset-id=c1-m2 \
   --worker min-count=0,max-count=2,resource-preset-id=c1-m2 \
   --triggerer count=1,resource-preset-id=c1-m2 \
   --dags-bucket course-work-bucket
