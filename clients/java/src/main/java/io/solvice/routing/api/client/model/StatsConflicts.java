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
import java.util.ArrayList;
import java.util.List;

/**
 * StatsConflicts
 */

public class StatsConflicts {

  @SerializedName("weight")
  private Integer weight = null;

  @SerializedName("reasons")
  private List<String> reasons = null;
  public StatsConflicts weight(Integer weight) {
    this.weight = weight;
    return this;
  }

  

  /**
  * Specific weight for unresolved goal reasons.
  * @return weight
  **/
  @Schema(description = "Specific weight for unresolved goal reasons.")
  public Integer getWeight() {
    return weight;
  }
  public void setWeight(Integer weight) {
    this.weight = weight;
  }
  public StatsConflicts reasons(List<String> reasons) {
    this.reasons = reasons;
    return this;
  }

  public StatsConflicts addReasonsItem(String reasonsItem) {
    if (this.reasons == null) {
      this.reasons = new ArrayList<String>();
    }
    this.reasons.add(reasonsItem);
    return this;
  }

  /**
  * Get reasons
  * @return reasons
  **/
  @Schema(description = "")
  public List<String> getReasons() {
    return reasons;
  }
  public void setReasons(List<String> reasons) {
    this.reasons = reasons;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    StatsConflicts statsConflicts = (StatsConflicts) o;
    return Objects.equals(this.weight, statsConflicts.weight) &&
        Objects.equals(this.reasons, statsConflicts.reasons);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(weight, reasons);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class StatsConflicts {\n");
    
    sb.append("    weight: ").append(toIndentedString(weight)).append("\n");
    sb.append("    reasons: ").append(toIndentedString(reasons)).append("\n");
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
