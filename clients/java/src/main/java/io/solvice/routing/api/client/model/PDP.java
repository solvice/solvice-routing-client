/*
 * OnRoute API
 * No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)
 *
 * OpenAPI spec version: 1.1.3
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

package io.solvice.routing.api.client.model;

import java.util.Objects;
import com.google.gson.TypeAdapter;
import com.google.gson.annotations.JsonAdapter;
import com.google.gson.annotations.SerializedName;
import com.google.gson.stream.JsonReader;
import com.google.gson.stream.JsonWriter;
import io.solvice.routing.api.client.model.Location;
import io.solvice.routing.api.client.model.Options;
import io.solvice.routing.api.client.model.Order;
import io.solvice.routing.api.client.model.SolveRequest;
import io.solvice.routing.api.client.model.Solver;
import io.solvice.routing.api.client.model.Vehicle;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * PDP
 */

public class PDP extends SolveRequest {

  @SerializedName("locations")
  private List<Location> locations = new ArrayList<Location>();

  @SerializedName("fleet")
  private List<Vehicle> fleet = new ArrayList<Vehicle>();

  @SerializedName("orders")
  private List<Order> orders = new ArrayList<Order>();

  @SerializedName("options")
  private Options options = null;
  public PDP locations(List<Location> locations) {
    this.locations = locations;
    return this;
  }

  public PDP addLocationsItem(Location locationsItem) {
    this.locations.add(locationsItem);
    return this;
  }

  /**
  * Get locations
  * @return locations
  **/
  @Schema(required = true, description = "")
  public List<Location> getLocations() {
    return locations;
  }
  public void setLocations(List<Location> locations) {
    this.locations = locations;
  }
  public PDP fleet(List<Vehicle> fleet) {
    this.fleet = fleet;
    return this;
  }

  public PDP addFleetItem(Vehicle fleetItem) {
    this.fleet.add(fleetItem);
    return this;
  }

  /**
  * Get fleet
  * @return fleet
  **/
  @Schema(required = true, description = "")
  public List<Vehicle> getFleet() {
    return fleet;
  }
  public void setFleet(List<Vehicle> fleet) {
    this.fleet = fleet;
  }
  public PDP orders(List<Order> orders) {
    this.orders = orders;
    return this;
  }

  public PDP addOrdersItem(Order ordersItem) {
    this.orders.add(ordersItem);
    return this;
  }

  /**
  * Get orders
  * @return orders
  **/
  @Schema(required = true, description = "")
  public List<Order> getOrders() {
    return orders;
  }
  public void setOrders(List<Order> orders) {
    this.orders = orders;
  }
  public PDP options(Options options) {
    this.options = options;
    return this;
  }

  

  /**
  * Get options
  * @return options
  **/
  @Schema(required = true, description = "")
  public Options getOptions() {
    return options;
  }
  public void setOptions(Options options) {
    this.options = options;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    PDP PDP = (PDP) o;
    return Objects.equals(this.locations, PDP.locations) &&
        Objects.equals(this.fleet, PDP.fleet) &&
        Objects.equals(this.orders, PDP.orders) &&
        Objects.equals(this.options, PDP.options) &&
        super.equals(o);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(locations, fleet, orders, options, super.hashCode());
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class PDP {\n");
    sb.append("    ").append(toIndentedString(super.toString())).append("\n");
    sb.append("    locations: ").append(toIndentedString(locations)).append("\n");
    sb.append("    fleet: ").append(toIndentedString(fleet)).append("\n");
    sb.append("    orders: ").append(toIndentedString(orders)).append("\n");
    sb.append("    options: ").append(toIndentedString(options)).append("\n");
    sb.append("}");
    return sb.toString();
  }

  /**
   * Convert the given object to string with each line indented by 4 spaces
   * (except the first line).
   */
  private String toIndentedString(java.lang.Object o) {
    if (o == null) {
      return "null";
    }
    return o.toString().replace("\n", "\n    ");
  }

}
