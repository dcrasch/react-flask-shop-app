var Constants = {
    FETCH_PRODUCT : "FETCH_PRODUCT"
};

var ProductStore = Fluxxor.createStore({
    initialize : function() {
	this.currentProduct = {};
	this.bindActions(
	    Constants.FETCH_PRODUCT, this.fetchProduct
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

var stores = {
    ProductStore : new ProductStore()
};
var actions = {
    fetchProduct : function(productid) {
	this.dispatch(Constants.FETCH_PRODUCT,{productid : productid});
    }
}

var FluxMixin = Fluxxor.FluxMixin(React);
var StoreWatchMixin = Fluxxor.StoreWatchMixin;

var FluxProduct = React.createClass({displayName: 'FluxProduct',
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
		React.createElement("h1", {className: "name"}, this.state.currentProduct.title)
	);
    }
});

var flux = new Fluxxor.Flux(stores, actions);

window.flux = flux;

React.render(
	React.createElement(FluxProduct, {flux: flux, productid: "1"}),
  document.getElementById('flux-product')
);
