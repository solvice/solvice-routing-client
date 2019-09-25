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
import io.solvice.routing.api.client.model.ApiErrorInner;
import io.swagger.v3.oas.annotations.media.Schema;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

/**
 * InputError
 */

public class InputError {

  @SerializedName("errors")
  private List<ApiErrorInner> errors = null;
  public InputError errors(List<ApiErrorInner> errors) {
    this.errors = errors;
    return this;
  }

  public InputError addErrorsItem(ApiErrorInner errorsItem) {
    if (this.errors == null) {
      this.errors = new ArrayList<ApiErrorInner>();
    }
    this.errors.add(errorsItem);
    return this;
  }

  /**
  * Get errors
  * @return errors
  **/
  @Schema(description = "")
  public List<ApiErrorInner> getErrors() {
    return errors;
  }
  public void setErrors(List<ApiErrorInner> errors) {
    this.errors = errors;
  }
  @Override
  public boolean equals(java.lang.Object o) {
    if (this == o) {
      return true;
    }
    if (o == null || getClass() != o.getClass()) {
      return false;
    }
    InputError inputError = (InputError) o;
    return Objects.equals(this.errors, inputError.errors);
  }

  @Override
  public int hashCode() {
    return java.util.Objects.hash(errors);
  }

  @Override
  public String toString() {
    StringBuilder sb = new StringBuilder();
    sb.append("class InputError {\n");
    
    sb.append("    errors: ").append(toIndentedString(errors)).append("\n");
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