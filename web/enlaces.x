1: {% url 'web:productosPorNombre' %} 
2: {% include 'includes/header_carrito.html' %}
3: en catalogo.html {% url 'web:producto' producto.id %}
4: en catalogo.html {% url 'web:producto' producto.id %}
5: en categorias.html {% url 'web:productosPorCategoria' categoria.id %}
6: en producto.html {% url 'web:agregarCarrito' producto.id %}
