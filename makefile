up:
	alembic upgrade head && \
	python generate_projects.py

start:
	cd app && \
	streamlit run app.py
