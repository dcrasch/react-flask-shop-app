jQuery.getJSON("/api/products/1", function(json) {

React.render(
	     <FluxProduct product={json} />,
	     document.getElementById('flux-product')
	     );
    });