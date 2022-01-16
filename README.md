# MyTaxi-project (how to use the mytaxi project?)
# steps: 

1 - pip install -r requirements.txt

# the order of use of the project
2 - driver and client creation

  2.1- http://127.0.0.1:8000/api/v1/driver/create/
  
  2.2- http://127.0.0.1:8000/api/v1/client/create/

3 - 4 different order statuses are created (create, cancel, accept, finish)  !!!Do not create statuses with other names.

4 - the driver is ordered by the client

4.1- http://127.0.0.1:8000/api/v1/order/create/

5- try using the status of the reservation

5.1- http://127.0.0.1:8000/api/v1/order/accept/

5.2- http://127.0.0.1:8000/api/v1/order/1/   (/1/->order_id)

6 - orders of clients in two time intervals

6.1- http://127.0.0.1:8000/api/v1/order/filter/1/?from=2021-12-06&to=2021-18-06   (/1/->client_id)


