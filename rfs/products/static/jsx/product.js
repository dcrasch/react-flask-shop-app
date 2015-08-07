var ProductClient = {
    load : function 
var ProductStore = Fluxxor.createStore({
    initialize : function() {
	this.loading = false;
	this.error = null;
	thi
var FluxProduct = React.createClass({
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
		<h1 className="name">{this.state.data.title}</h1>
	);
    }
});
