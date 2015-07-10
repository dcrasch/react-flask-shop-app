var FluxProduct = React.createClass({displayName: 'FluxProduct',
    render: function() {
	return (
		React.createElement("h1", {className: "name"}, this.props.product.title)
	);
    }
});

jQuery.getJSON("/api/products/1", function(json) {

React.render(
	     React.createElement(FluxProduct, {product: json}),
	     document.getElementById('flux-product')
	     );
    });