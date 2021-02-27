CREATE TABLE cleaned_table AS 
  (SELECT b.address, b.city, b.state, b.postal_code,b.latitude,b.longitude,b.stars, b.review_count, b.is_open,
          a.*
   FROM business_table as b
   INNER JOIN attributes_table a
   ON b.business_id = a.business_id);
   