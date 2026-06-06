-- public.receipts определение

-- Drop table

-- DROP TABLE receipts;

CREATE TABLE receipts (
	id serial4 NOT NULL,
	doc_id varchar(16) NULL,
	cass_id int4 NOT NULL,
	total_price numeric NOT NULL,
	created_at timestamp NULL,
	CONSTRAINT receipts_pkey PRIMARY KEY (id)
);
CREATE INDEX ix_receipts_doc_id ON public.receipts USING btree (doc_id);
CREATE INDEX ix_receipts_id ON public.receipts USING btree (id);


-- public.receipts внешние включи

ALTER TABLE public.receipts ADD CONSTRAINT receipts_cass_id_fkey FOREIGN KEY (cass_id) REFERENCES casses(id);