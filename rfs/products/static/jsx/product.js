var FluxProduct = React.createClass({
	getInitialState: function() {
	    return {product: []};
	},
	componentDidMount: function() {
	    $.ajax({
		    url: this.props.url,
		    dataType: 'json',
		    cache: false,
		    success: function(data) {
			this.setState({product: data});
		    }.bind(this),
		    error: function(xhr, status, err) {
			console.error(this.props.url, status, err.toString());
		    }.bind(this)
		});
	},
    render: function() {
	return (
		<h1 className="name">{this.state.product.title}</h1>
	);
    }
});
