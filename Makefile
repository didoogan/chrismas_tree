devrun:
	@docker-compose up -d
down:
	@docker-compose down --remove-orphans
grun:
	@docker run --rm -p 80:5000 didoogan/chrismas_tree
