/* initialize fluxxor */

var flux = new Fluxxor.Flux();
window.flux = flux;
var FluxMixin = Fluxxor.FluxMixin(React);
var StoreWatchMixin = Fluxxor.StoreWatchMixin;



var product_constants = {
    FETCH_PRODUCT : 'FETCH_PRODUCT'
};

var ProductStore = Fluxxor.createStore({
    
    initialize : function() {
	this.currentProduct = {};
	this.bindActions(
	    product_constants.FETCH_PRODUCT, this.fetchProduct
	);
    },
    
    fetchProduct: function(payload) {
	var that = this;
	jQuery.getJSON(
	    "/api/products/"+payload.productid,
	    function(data) {
		that.currentProduct=data;
		that.emit('change');
	    });	
	//return this.emit('change');
    },
    
    getState : function() {
	return {
	    currentProduct : this.currentProduct
	};
    }
    
});

flux.addStore("ProductStore", new ProductStore());
flux.addAction("fetchProduct", function(productid) {
    this.dispatch(product_constants.FETCH_PRODUCT,{productid : productid});
});

var FluxProduct = React.createClass({
    mixins : [FluxMixin, StoreWatchMixin('ProductStore')],
    getInitialSate : function() {
	return {}
    },
	    
    getStateFromFlux: function() {
	var flux = this.getFlux();
	return flux.store('ProductStore').getState();
    },
    
    componentDidMount: function() {
	this.getFlux().actions.fetchProduct(this.props.productid);
    },
    
    render: function() {
	return (
		<h1 className="name">{this.state.currentProduct.title}</h1>
	);
    }
});
