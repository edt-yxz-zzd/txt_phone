/*
e ./script/finger_tree/finger_tree.cpp
view others/数学/编程/tree/finger_tree.txt

最终约束
  #由来 见下面safe
  +[2 <= min nd <= max nd <= max dg -min dg]
    约束甲
    #错:其实可以放宽，因为达到(1+max dg)后，可以拆成多个Node，max dg 不用太大
    #   单Node补充，单Node进位
  +[min nd <= 2*min dg][nd值可以组成[2*min dg..]的所有值]
    约束乙
  变量说明:
    nd 即 Node 的各种可能大小#下文给出[2..3]
    dg 即 Digit 的各种可能大小#下文给出[1..4]
  可选方案:
    0: nd<-[2,3], dg <-[1..>=4]
    1: nd<-[3,4], dg <-[3..>=7]
    2: nd<-[2,5], dg <-[2..>=7]
    3: nd<-[3,5], dg <-[4..>=9]
    4: nd<-[3,4,5], dg <-[2..>=7]
    5: nd<-[4,5,6,7], dg <-[2..>=9]
        nd<-[4,5,6,7], dg <-[2..10]
          2..5..7..10





*/

namespace nn_ns {
typedef unsigned int uint;

class setting4finger_tree
{
  static const
    uint num_node_kind = 2;
  static const
    uint sorted_sizes4node[num_node_kind] = {2,3};

  static const
    uint min_size4digit = 1;
  static const
    uint max_size4digit = 4;

  uint decompose_into_nodes(uint sz_ge_2_min_digit);
};

template <class setting4finger_tree>
constexpr bool check__setting4finger_tree()
{
  typedef setting4finger_tree T;
  static_assert type_eq<uint>(T::num_node_kind);
  static_assert type_eq<uint [T::num_node_kind]>(T::sorted_sizes4node);
  static_assert type_eq<uint>(T::min_size4digit);
  static_assert type_eq<uint>(T::max_size4digit);

  static_assert 2 <= T::num_node_kind;
  static_assert is_strict_sorted(T::sorted_sizes4node);
  static_assert 1 == gcd(T::sorted_sizes4node);
  static_assert 2 <= T::sorted_sizes4node[0];
  static_assert T::sorted_sizes4node[num_node_kind-1] <= T::max_size4digit -T::min_size4digit;
  static_assert T::sorted_sizes4node[0] <= 2*T::min_size4digit;
  static_assert check__decompose_into_nodes<T>(2*T::min_size4digit, T::sorted_sizes4node[num_node_kind-1]);
    // check decompose_into_nodes(sz) for sz in [2*min_dg..=max_nd]
}

template <class setting4finger_tree>
class finger_tree
{
  static_assert check__setting4finger_tree<setting4finger_tree>();
};


} // namespace nn_ns
