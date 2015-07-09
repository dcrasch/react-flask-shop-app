var FluxProduct = React.createClass({displayName: 'FluxProduct',
    render: function() {
	return (
		React.createElement("div", null, "Hello world")
	);
    }
});

React.render(
	     React.createElement(FluxProduct, null),
	     document.getElementById('flux-product')
	     );