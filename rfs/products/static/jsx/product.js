var ProductStore = Fluxxor.createStore({
    actions : {
	"FETCH_PRODUCT" : "fetchProduct",
    },
    initialize : function() {
	this.currentProduct = {};
    },
    fetchProduct: function(payload) {
	request
	    .get(AppCfg.apiURL+"/api/products/"+payload.productid)
	    .accept('json')
	    .end(function(error,res) {
		if (res.status == 200) {
		    this.currentProduct=res.body;
		}
	    }.bind(this));
	return this.emit('change');
    },
    getState : function() {
	return {
	    currentProduct : this.currentProduct
	};
    }
});


var FluxMixin = Fluxxor.FluxMixin(React);
var StoreWatchMixin = Fluxxor.StoreWatchMixin;

var FluxProduct = React.createClass({
    mixins : [FluxMixin, StoreWatchMixin('ProductStore')],
    getInitialSate : function() {
	return {}
    },
	    
    getStateFromFlux: function() {
	return this.getFlux().store('ProductStore').getState();
    },
    
    componentDidMount: function() {
	this.getFlux().actions.loadProduct(this.props.productid);
    },
    
    render: function() {
	return (
		<h1 className="name">{this.state.data.title}</h1>
	);
    }
});
