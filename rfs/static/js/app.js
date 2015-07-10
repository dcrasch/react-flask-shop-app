var FluxProduct = React.createClass({displayName: 'FluxProduct',
	getInitialState: function() {
	    return {data: []};
	},
	componentDidMount: function() {
	    $.ajax({
		    url: this.props.url,
		    dataType: 'json',
		    cache: false,
		    success: function(data) {
			this.setState({data: data});
		    }.bind(this),
		    error: function(xhr, status, err) {
			console.error(this.props.url, status, err.toString());
		    }.bind(this)
		});
	},
    render: function() {
	return (
		React.createElement("h1", {className: "name"}, this.state.data.title)
	);
    }
});

React.render(
  React.createElement(FluxProduct, {url: "/api/products/1"}),
  document.getElementById('flux-product')
);
