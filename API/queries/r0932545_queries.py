get_testimonials_query = "SELECT * FROM wedding.testimonial;"

get_portfolios_sorted_with_id_query = "SELECT * FROM wedding.portfolio WHERE id = %(id)s;"

insert_contact_form_query = """
    INSERT INTO wedding.contactform (id,name,email,message)
    VALUES (%(id)s,%(name)s,%(email)s,%(message)s)
"""
