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
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;

/**
 * Break definitions
 */
@Schema(description = "Break definitions")
public class VehicleBreaks {

  @SerializedName("breakstart")
  private Integer breakstart = null;

  @SerializedName("breakend")
  private Integer breakend = null;

  @SerializedName("breakduration")
  private Integer breakduration = null;
  public VehicleBreaks breakstart(Integer breakstart) {
    this.breakstart = breakstart;
    return this;
  }

  

  /**
  * Earliest starting time of break
  * minimum: 0
  * maximum: 1439
  * @return breakstart
  **/
  @Schema(example = "780", required = true, description = "Earliest starting time of break")
  public Integer getBreakstart() {
    return breakstart;
  }
  public void setBreakstart(Integer breakstart) {
    this.breakstart = breakstart;
  }
  public VehicleBreaks breakend(Integer breakend) {
    this.breakend = breakend;
    return this;
  }

  

  /**
  * Earliest ending time of break.
  * minimum: 0
  * maximum: 1439
  * @return breakend
  **/
  @Schema(example = "860", required = true, description = "Earliest ending time of break.")
  public Integer getBreakend() {
    return breakend;
  }
  public void setBreakend(Integer breakend) {
    this.breakend = breakend;
  }
  public VehicleBreaks breakduration(Integer breakduration) {
    this.breakduration = breakduration;
    return this;
  }

  

  /**
  * Duration of break, should be less than end minus start.
  * minimum: 0
  * maximum: 1439
  * @return breakduration
  **/
  @Schema(example = "30", required = true, description = "Duration of break, should be less than end minus start.")
  public Integer getBreakduration() {
    return breakduration;
  }
  public void setBreakduration(Integer breakduration) {
    this.breakduration = breakduration;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    VehicleBreaks vehicleBreaks = (VehicleBreaks) o;
    return Objects.equals(this.breakstart, vehicleBreaks.breakstart) &&
        Objects.equals(this.breakend, vehicleBreaks.breakend) &&
        Objects.equals(this.breakduration, vehicleBreaks.breakduration);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(breakstart, breakend, breakduration);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class VehicleBreaks {\n");
    
    sb.append("    breakstart: ").append(toIndentedString(breakstart)).append("\n");
    sb.append("    breakend: ").append(toIndentedString(breakend)).append("\n");
    sb.append("    breakduration: ").append(toIndentedString(breakduration)).append("\n");
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
